# Third Party Library
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles

# Project Stuff
from core.app_config import app_config
from routes import router as api_router

app = FastAPI(
    title='Test',
    description='Test',
    version='0.1.0',
    terms_of_service='http://example.com/terms/',
)

app.include_router(api_router)
app.openapi_version = "3.0.0"
app.mount('/static', StaticFiles(directory='src/core/static'), name='static')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8003"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', include_in_schema=False)
def custom_swagger_ui_html():
    return get_swagger_ui_html(
        title='Predict API',
        openapi_url=f'.{app.openapi_url}',
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url='./static/swagger-ui-bundle.js',
        swagger_css_url='./static/swagger-ui.css',
    )



if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=app_config.service_host,
        port=app_config.service_port,
        reload=True,
    )
