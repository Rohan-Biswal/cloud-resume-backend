from google.cloud import firestore
from flask import jsonify

db = firestore.Client()

def visitor_counter(request):
    # Handle CORS preflight request
    if request.method == "OPTIONS":
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        }
        return ("", 204, headers)

    doc_ref = db.collection("visitors").document("counter")
    doc = doc_ref.get()

    if doc.exists:
        count = doc.to_dict().get("count", 0) + 1
    else:
        count = 1

    doc_ref.set({"count": count})

    headers = {
        "Access-Control-Allow-Origin": "*"
    }
    
    # CI/CD Test Trigger 1
    return (
        jsonify({"visitor_count": count}),
        200,
        headers
    )
