from fastapi import HTTPException, Header

def verify_token(authorization: str = Header(None)):
    if authorization != "Bearer SECRET123":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"user": "authenticated"}
