import json
import boto3
import numpy as np
from PIL import Image, ImageFilter
import io
import os
import time
import logging
from typing import Dict, Tuple, List, Any
from datetime import datetime

# Initialize AWS services
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
cloudwatch = boto3.client('cloudwatch')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Get environment variables
BUCKET_NAME = os.environ['BUCKET_NAME']
TABLE_NAME = os.environ['TABLE_NAME']
table = dynamodb.Table(TABLE_NAME)

def put_metric(name: str, value: float) -> None:
    """Send custom metric to CloudWatch"""
    try:
        cloudwatch.put_metric_data(
            Namespace='ImageProcessing',
            MetricData=[{
                'MetricName': name,
                'Value': value,
                'Unit': 'None'
            }]
        )
    except Exception as e:
        logger.error(f"Error putting metric {name}: {str(e)}")

def load_image_from_s3(bucket: str, key: str) -> Tuple[Image.Image, str]:
    """Load image from S3 bucket"""
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        image_data = response['Body'].read()
        image = Image.open(io.BytesIO(image_data))
        return image, response['ContentType']
    except Exception as e:
        logger.error(f"Error loading image from S3: {str(e)}")
        raise

def save_image_to_s3(image: Image.Image, bucket: str, key: str, content_type: str) -> str:
    """Save processed image back to S3"""
    try:
        buffer = io.BytesIO()
        image.save(buffer, format=image.format or 'JPEG')
        buffer.seek(0)
        s3.put_object(
            Bucket=bucket,
            Key=key,
            Body=buffer,
            ContentType=content_type
        )
        return f"s3://{bucket}/{key}"
    except Exception as e:
        logger.error(f"Error saving image to S3: {str(e)}")
        raise

def randomize_and_obscure_slices(
    img: Image.Image,
    min_slice_height: int = 15,
    max_slice_height: int = 30
) -> Tuple[np.ndarray, List[Dict[str, Any]]]:
    """Process image with randomized slices and blur effects"""
    try:
        img_array = np.array(img)
        h, w, _ = img_array.shape
        
        # Initialize slices and metadata
        slices = []
        slice_metadata = []
        y = 0
        
        # Create variable height slices
        while y < h:
            slice_height = np.random.randint(min_slice_height, max_slice_height)
            if y + slice_height > h:
                slice_height = h - y
            
            slice_section = img_array[y:y + slice_height, :]
            slices.append(slice_section)
            
            # Store metadata for each slice
            slice_metadata.append({
                'y_position': y,
                'height': slice_height,
                'blur_applied': False
            })
            
            y += slice_height
        
        # Shuffle slices with tracking
        indices = list(range(len(slices)))
        np.random.shuffle(indices)
        shuffled_slices = [slices[i] for i in indices]
        
        # Apply blur effects and update metadata
        for i, slice_section in enumerate(shuffled_slices):
            if np.random.random() < 0.3:
                slice_img = Image.fromarray(slice_section)
                blurred_slice = slice_img.filter(ImageFilter.GaussianBlur(radius=5))
                shuffled_slices[i] = np.array(blurred_slice)
                slice_metadata[indices[i]]['blur_applied'] = True
        
        # Reassemble image
        processed_img = np.vstack(shuffled_slices)
        
        return processed_img, slice_metadata
    except Exception as e:
        logger.error(f"Error processing image: {str(e)}")
        raise

def save_metadata(
    image_id: str,
    original_key: str,
    processed_key: str,
    slice_metadata: List[Dict[str, Any]]
) -> None:
    """Save processing metadata to DynamoDB"""
    try:
        timestamp = int(time.time())
        table.put_item(Item={
            'imageId': image_id,
            'timestamp': timestamp,
            'originalKey': original_key,
            'processedKey': processed_key,
            'sliceMetadata': slice_metadata,
            'processingDate': datetime.utcnow().isoformat()
        })
    except Exception as e:
        logger.error(f"Error saving metadata: {str(e)}")
        raise

def handler(event, context):
    """Main Lambda handler"""
    try:
        start_time = time.time()
        
        # Parse input
        body = json.loads(event['body']) if isinstance(event.get('body'), str) else event.get('body', {})
        image_key = body.get('image_key')
        
        if not image_key:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'No image key provided'})
            }
        
        # Load image
        image, content_type = load_image_from_s3(BUCKET_NAME, image_key)
        
        # Process image
        processed_array, slice_metadata = randomize_and_obscure_slices(image)
        processed_image = Image.fromarray(processed_array)
        
        # Save processed image
        processed_key = f"processed/{os.path.basename(image_key)}"
        output_url = save_image_to_s3(processed_image, BUCKET_NAME, processed_key, content_type)
        
        # Save metadata
        image_id = os.path.splitext(os.path.basename(image_key))[0]
        save_metadata(image_id, image_key, processed_key, slice_metadata)
        
        # Record metrics
        processing_time = time.time() - start_time
        put_metric('ProcessingTime', processing_time)
        put_metric('SliceCount', len(slice_metadata))
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Image processed successfully',
                'imageId': image_id,
                'outputUrl': output_url,
                'processingTime': processing_time,
                'sliceCount': len(slice_metadata)
            })
        }
        
    except Exception as e:
        logger.error(f"Error in handler: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Internal server error',
                'message': str(e)
            })
        }