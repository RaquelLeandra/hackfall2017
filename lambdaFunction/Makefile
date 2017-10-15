
PROJECT = readist
VIRTUAL_ENV = env
FUNCTION_NAME = readist
AWS_REGION = eu-3
FUNCTION_HANDLER = lambda_handler
LAMBDA_ROLE = arn:aws:iam::753544318504:role/service-role/BasicRole

# Default commands
install: virtual


virtual: \
    #@echo "--> set up and activate virtualenv" \
    if test ! -d "$(VIRTUAL_ENV)"; then \
        pip install virtualenv; \
        virtualenv $(VIRTUAL_ENV); \
    fi \
    @echo ""
