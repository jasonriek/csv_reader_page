# csv_reader_page
A simple http page for reading CSV files to a table using Python as a backend.

# CSV Reader FastAPI Service Setup

This guide explains how to set up and run the CSV Reader FastAPI service on a **Ubuntu** or **RHEL** server. The service will be managed using **systemd** to ensure it runs continuously and starts on boot.

## **1️⃣ Prerequisites**

Ensure your system has:
- **Python 3.8+** installed.
- **pip** and **venv** for managing dependencies.
- **Uvicorn** for running the FastAPI app.

## **2️⃣ Install Required Packages**

### **Ubuntu**
```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip
```

### **RHEL**
```bash
sudo yum install -y python3 python3-venv python3-pip
```

## **3️⃣ Clone the Repository & Set Up Virtual Environment**

```bash
cd /home/jasonr/dev/
git clone https://github.com/your-repo/csv_reader_page.git
cd csv_reader_page

# Create and activate virtual environment
python3 -m venv csv_reader_page_venv
source csv_reader_page_venv/bin/activate
```

## **4️⃣ Install Dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Ensure `requirements.txt` includes:
```
fastapi
uvicorn
jinja2
```

## **5️⃣ Test Running the Application Manually**

Before setting it up as a service, test that it runs correctly:
```bash
uvicorn main:app --host 0.0.0.0 --port 51991
```
Check by visiting: `http://your-server-ip:51991/`

Press `CTRL+C` to stop the process.

---

## **6️⃣ Create a Systemd Service**

Create a service file:
```bash
sudo nano /etc/systemd/system/csv_reader.service
```

Add the following content:
```ini
[Unit]
Description=CSV Reader FastAPI Service
After=network.target

[Service]
User=jasonr
Group=jasonr
WorkingDirectory=/home/jasonr/dev/csv_reader_page
ExecStart=/home/jasonr/dev/csv_reader_page/csv_reader_page_venv/bin/uvicorn main:app --host 0.0.0.0 --port 51991
Restart=always

[Install]
WantedBy=multi-user.target
```

Save and exit (`CTRL+X`, then `Y`, then `ENTER`).

## **7️⃣ Enable & Start the Service**

```bash
sudo systemctl daemon-reload
sudo systemctl enable csv_reader.service
sudo systemctl start csv_reader.service
sudo systemctl status csv_reader.service
```

Check logs if needed:
```bash
journalctl -u csv_reader.service -f
```

## **9️⃣ Managing the Service**

To **restart** the service:
```bash
sudo systemctl restart csv_reader.service
```

To **stop** the service:
```bash
sudo systemctl stop csv_reader.service
```

To **check status**:
```bash
sudo systemctl status csv_reader.service
```

To **disable it from starting on boot**:
```bash
sudo systemctl disable csv_reader.service
```

---

## **✅ Done!**
Your CSV Reader FastAPI service should now be running as a background process.
