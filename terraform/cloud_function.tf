resource "google_cloudfunctions2_function" "visitor_counter" {
  name     = "visitor-counter"
  location = var.region

  build_config {
    runtime     = "python311"
    entry_point = "visitor_counter"

    source {
      storage_source {
        bucket = google_storage_bucket.function_bucket.name
        object = google_storage_bucket_object.function_zip.name
      }
    }
  }

  service_config {
    max_instance_count    = 1
    available_memory      = "256M"
    timeout_seconds       = 60
    ingress_settings      = "ALLOW_ALL"
    service_account_email = google_service_account.resume_function_sa.email
  }
}
