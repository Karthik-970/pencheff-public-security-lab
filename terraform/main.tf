resource "aws_s3_bucket" "lab_bucket" {
  bucket = "pencheff-public-security-lab-example"

  tags = {
    Name = "Pencheff Security Lab"
  }
}

resource "aws_s3_bucket_public_access_block" "lab_bucket" {
  bucket = aws_s3_bucket.lab_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}
