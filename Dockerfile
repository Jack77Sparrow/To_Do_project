FROM python:3.12-bullseye

# Робоча директорія
WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt .

# Встановлюємо cron і bash
RUN apt-get update && apt-get install -y cron bash && rm -rf /var/lib/apt/lists/*

# Встановлюємо залежності Python
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект
COPY . .

# Копіюємо crontab файл у контейнер (створи його як mycron у проекті)
COPY mycron /etc/cron.d/mycron
RUN chmod 0644 /etc/cron.d/mycron
RUN crontab /etc/cron.d/mycron

# Виставляємо порт для uvicorn
EXPOSE 8000

# Запуск cron в передньому плані та uvicorn через & (фоновий процес)
CMD cron && uvicorn UI.web_interface.WEB_interface:app --host 0.0.0.0 --port 8000
