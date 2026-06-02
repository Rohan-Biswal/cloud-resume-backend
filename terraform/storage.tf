resource "google_storage_bucket_object" "function_zip" {
  name   = "function.zip"
  bucket = google_storage_bucket.function_bucket.name
  source = "../function.zip"
}
