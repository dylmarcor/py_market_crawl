from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

# Add logic for POST/GET for symbols
@router.get("/symbols")
def symbol_check():
    return {"status": "ok"}