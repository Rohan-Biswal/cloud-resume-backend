resource "google_service_account" "resume_function_sa" {
  account_id   = "resume-function-sa"
  display_name = "Resume Function Service Account"
}

resource "google_project_iam_member" "firestore_user" {
  project = var.project_id
  role    = "roles/datastore.user"
  member  = "serviceAccount:${google_service_account.resume_function_sa.email}"
}