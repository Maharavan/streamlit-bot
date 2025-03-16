from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
app = FastAPI()

try:
    model = AutoModelForCausalLM.from_pretrained('deepseek-ai/DeepSeek-V3', torch_dtype=torch.float32, trust_remote_code=True)
    tokenizer = AutoTokenizer.from_pretrained('deepseek-ai/DeepSeek-V3', trust_remote_code=True)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=-1)  # Use CPU
except Exception as e:
    print(f"❌ Error loading model: {str(e)}")
    pipe = None 

class InputData(BaseModel):
    text: str

@app.post("/process/")
async def process_data(data: InputData):
    if pipe is None:
        raise HTTPException(status_code=500, detail="Model not available. Check server logs.")

    try:
        # ✅ Use the model safely
        result = pipe(data.text, max_length=200, num_return_sequences=1)
        return {"generated_text": result[0]["generated_text"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating text: {str(e)}")
