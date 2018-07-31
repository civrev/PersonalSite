#This script sets up my personal website with Azure, to be run in AzureCLI

#Makes a new resource group, and assigns the region for it
az group create --name PersonalWebsite --location "Central US"

#sets up the app service plan (F1 is free, but not available for linux (needed for Python))
#app service plan is basically setting up resource demands
az appservice plan create --name personalWebServer --resource-group PersonalWebsite --sku B1 --is-linux

#deploys a web app from the docker container I set up
az webapp create --resource-group PersonalWebsite --plan personalWebServer --name cwatts --deployment-container-image-name civrev/flask-quickstart

#open up port 8000 as was done in the container
#cwatts is my name! Get your own!
az webapp config appsettings set --name cwatts --resource-group PersonalWebsite --settings WEBSITES_PORT=8000
