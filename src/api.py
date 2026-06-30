
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

import asyncio, requests

router = FastAPI()

@router.get("/scan")
async def scan_url(request : Request) -> None:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get('https://www.youtube.com', headers=headers)
    print(response.content)

    return

@router.post("/register")
async def register_user(request : Request) -> None:
    return


