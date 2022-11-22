web: uvicorn app.main:app --workers 4 --host 0.0.0.0 --port=${PORT:-5000}
postdeploy: alembic upgrade head
