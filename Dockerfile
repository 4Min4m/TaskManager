#Python
FROM python:3.11-slim

#WorkDirectory
WORKDIR /app

#CopyToContainer
COPY . .

#InstallDependencies
RUN pip install --no-cache-dir -r requirments.txt

#Open5000Port
EXPOSE 5000

#RunApplication
CMD [ "python", "app.py" ]