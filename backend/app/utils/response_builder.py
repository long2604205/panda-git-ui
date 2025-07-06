def build_response(result):
    if result.get("success"):
        return {
            "status": "success",
            "data": result["data"]
        }
    else:
        return {
            "status": "error",
            "message": result.get("error", "Unknown error")
        }
