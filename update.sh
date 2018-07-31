#This code redeploys the docker image to the Azure web app

#to update the site, push the docker container and then run this
#cwatts is my name, get your own!
az webapp restart --resource-group PersonalWebsite --name cwatts
