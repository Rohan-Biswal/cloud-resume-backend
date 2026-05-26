from google.cloud import firestore
from flask import jsonify

db = firestore.Client()

def visitor_counter(request):
    doc_ref = db.collection("visitors").document("counter")

    doc = doc_ref.get()

    if doc.exists:
        count = doc.to_dict().get("count", 0)
        count += 1
    else:
        count = 1

    doc_ref.set({
        "count": count
    })

    return jsonify({
        "visitor_count": count
    })