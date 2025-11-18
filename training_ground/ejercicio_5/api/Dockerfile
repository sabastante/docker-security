# Small, maintained base
FROM python:3.12-slim

# Safety + predictable stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create an unprivileged user and working dir
RUN adduser --system --group --home /app appuser
WORKDIR /app

# Install deps first to leverage build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Drop root
USER appuser

# Documented port (publish with -p at runtime)
EXPOSE 8080

# Run with Gunicorn (no dev server)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app", "--workers", "2", "--threads", "4", "--timeout", "60"]
