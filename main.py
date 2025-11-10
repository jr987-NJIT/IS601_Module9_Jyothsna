# main.py

from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field, field_validator
from fastapi.exceptions import RequestValidationError
from app.operations import add, subtract, multiply, divide
from app.database import get_db, init_db, User, Calculation
from sqlalchemy.orm import Session
import uvicorn
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    logger.info("Initializing database...")
    init_db()
    logger.info("Database initialized successfully")

# Setup templates directory
templates = Jinja2Templates(directory="templates")

# Pydantic model for request data
class OperationRequest(BaseModel):
    a: float = Field(..., description="The first number")
    b: float = Field(..., description="The second number")
    username: str = Field(default="anonymous", description="Username performing the operation")

    @field_validator('a', 'b')
    def validate_numbers(cls, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Both a and b must be numbers.')
        return value

# Pydantic model for successful response
class OperationResponse(BaseModel):
    result: float = Field(..., description="The result of the operation")
    calculation_id: int = Field(None, description="Database ID of the calculation")
    message: str = Field(default="Operation completed successfully")

# Pydantic model for error response
class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")

# Custom Exception Handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTPException on {request.url.path}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Extracting error messages
    error_messages = "; ".join([f"{err['loc'][-1]}: {err['msg']}" for err in exc.errors()])
    logger.error(f"ValidationError on {request.url.path}: {error_messages}")
    return JSONResponse(
        status_code=400,
        content={"error": error_messages},
    )

@app.get("/")
async def read_root(request: Request):
    """
    Serve the index.html template.
    """
    logger.info("Serving index.html")
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring and Docker healthcheck.
    """
    logger.info("Health check requested")
    return {"status": "healthy", "message": "FastAPI Calculator is running"}

def save_calculation_to_db(db: Session, username: str, operation: str, a: float, b: float, result: float):
    """
    Helper function to save calculation to database.
    Creates user if doesn't exist, then saves calculation.
    """
    try:
        # Check if user exists, create if not
        user = db.query(User).filter(User.username == username).first()
        if not user:
            # Create user with email based on username
            user = User(username=username, email=f"{username}@calculator.com")
            db.add(user)
            db.commit()
            db.refresh(user)
            logger.info(f"Created new user: {username}")
        
        # Create calculation record
        calc = Calculation(
            operation=operation,
            operand_a=a,
            operand_b=b,
            result=result,
            user_id=user.id
        )
        db.add(calc)
        db.commit()
        db.refresh(calc)
        logger.info(f"Saved calculation ID {calc.id} for user {username}")
        return calc.id
    except Exception as e:
        db.rollback()
        logger.error(f"Database error: {str(e)}")
        return None

@app.post("/add", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def add_route(operation: OperationRequest, db: Session = Depends(get_db)):
    """
    Add two numbers and save to database.
    """
    logger.info(f"Add API called with a={operation.a}, b={operation.b}, user={operation.username}")
    try:
        result = add(operation.a, operation.b)
        calc_id = save_calculation_to_db(db, operation.username, "add", operation.a, operation.b, result)
        logger.info(f"Add operation successful: {operation.a} + {operation.b} = {result}")
        return OperationResponse(
            result=result, 
            calculation_id=calc_id,
            message=f"Addition saved to database (ID: {calc_id})"
        )
    except Exception as e:
        logger.error(f"Add Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/subtract", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def subtract_route(operation: OperationRequest, db: Session = Depends(get_db)):
    """
    Subtract two numbers and save to database.
    """
    logger.info(f"Subtract API called with a={operation.a}, b={operation.b}, user={operation.username}")
    try:
        result = subtract(operation.a, operation.b)
        calc_id = save_calculation_to_db(db, operation.username, "subtract", operation.a, operation.b, result)
        logger.info(f"Subtract operation successful: {operation.a} - {operation.b} = {result}")
        return OperationResponse(
            result=result,
            calculation_id=calc_id,
            message=f"Subtraction saved to database (ID: {calc_id})"
        )
    except Exception as e:
        logger.error(f"Subtract Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/multiply", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def multiply_route(operation: OperationRequest, db: Session = Depends(get_db)):
    """
    Multiply two numbers and save to database.
    """
    logger.info(f"Multiply API called with a={operation.a}, b={operation.b}, user={operation.username}")
    try:
        result = multiply(operation.a, operation.b)
        calc_id = save_calculation_to_db(db, operation.username, "multiply", operation.a, operation.b, result)
        logger.info(f"Multiply operation successful: {operation.a} * {operation.b} = {result}")
        return OperationResponse(
            result=result,
            calculation_id=calc_id,
            message=f"Multiplication saved to database (ID: {calc_id})"
        )
    except Exception as e:
        logger.error(f"Multiply Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/divide", response_model=OperationResponse, responses={400: {"model": ErrorResponse}})
async def divide_route(operation: OperationRequest, db: Session = Depends(get_db)):
    """
    Divide two numbers and save to database.
    """
    logger.info(f"Divide API called with a={operation.a}, b={operation.b}, user={operation.username}")
    try:
        result = divide(operation.a, operation.b)
        calc_id = save_calculation_to_db(db, operation.username, "divide", operation.a, operation.b, result)
        logger.info(f"Divide operation successful: {operation.a} / {operation.b} = {result}")
        return OperationResponse(
            result=result,
            calculation_id=calc_id,
            message=f"Division saved to database (ID: {calc_id})"
        )
    except ValueError as e:
        logger.error(f"Divide Operation Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Divide Operation Internal Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# New endpoint to get calculation history
@app.get("/calculations")
async def get_calculations(db: Session = Depends(get_db), limit: int = 10):
    """
    Get recent calculations from database.
    """
    try:
        calculations = db.query(Calculation).order_by(Calculation.timestamp.desc()).limit(limit).all()
        return {
            "count": len(calculations),
            "calculations": [
                {
                    "id": calc.id,
                    "operation": calc.operation,
                    "operand_a": calc.operand_a,
                    "operand_b": calc.operand_b,
                    "result": calc.result,
                    "timestamp": calc.timestamp,
                    "user_id": calc.user_id
                }
                for calc in calculations
            ]
        }
    except Exception as e:
        logger.error(f"Error fetching calculations: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching calculations")

# New endpoint to get users
@app.get("/users")
async def get_users(db: Session = Depends(get_db)):
    """
    Get all users from database.
    """
    try:
        users = db.query(User).all()
        return {
            "count": len(users),
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "created_at": user.created_at,
                    "calculation_count": len(user.calculations)
                }
                for user in users
            ]
        }
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        raise HTTPException(status_code=500, detail="Error fetching users")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
