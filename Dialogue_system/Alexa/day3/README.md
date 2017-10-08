# Upload zip file on Amazon Lambda

> reference : http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

example : using library request.

1. create directory "alexa-lambda"
2. go to command line, type >> pip install requests PATH/alexa-lambda

picture1

then you will see

picture2

then upload zip file. (alexa-lambda.zip)

test with matching intent. and fix "Handler" for ---[.py].lambda_handler. <br/>
e.g.m Handler : index.lambda_handler (index from index.py, lambda_handler is main function in index.py)

pic3

pic4
