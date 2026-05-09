from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import asyncio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
}

@app.get("/")
async def root():
    return {"status": "Nifty Proxy Live 🔥", "endpoints": ["/nifty", "/options", "/fii"]}

@app.get("/nifty")
async def get_nifty():
    try:
        async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
            await client.get("https://www.nseindia.com", timeout=10)
            r = await client.get(
                "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050",
                timeout=15
            )
            return r.json()
    except Exception as e:
        return {"error": str(e)}

@app.get("/options")
async def get_options():
    try:
        async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
            await client.get("https://www.nseindia.com", timeout=10)
            r = await client.get(
                "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY",
                timeout=15
            )
            return r.json()
    except Exception as e:
        return {"error": str(e)}

@app.get("/fii")
async def get_fii():
    try:
        async with httpx.AsyncClient(headers=HEADERS, follow_redirects=True) as client:
            await client.get("https://www.nseindia.com", timeout=10)
            r = await client.get(
                "https://www.nseindia.com/api/fiidiiTradeReact",
                timeout=15
            )
            return r.json()
    except Exception as e:
        return {"error": str(e)}
