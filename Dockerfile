FROM public.ecr.aws/lambda/python:3.12

RUN mkdir -p /app 
# here you are just copying the files required for you to run the container
# ofcourse we need the main file, that goes inside the app directory we created above,
# it will be named the same as we left it empty
COPY ./main.py /app/
# then we copy requirements file to install all dependencies
COPY ./requirements.txt /app/requirements.txt
#then we copy the folder, all the content from host machine will be copied as it is onto app 
COPY mylib/ /app/mylib/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD ["main.py"]
ENTRYPOINT ["python"]