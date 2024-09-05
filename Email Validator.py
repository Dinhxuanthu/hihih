class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name: str) -> bool:
       
        return len(name) >= self.min_length

    def __validate_mail(self, mail: str) -> bool:
       
        return mail in self.mails

    def __validate_domain(self, domain: str) -> bool:
      
        return domain in self.domains

    def validate(self, email: str) -> bool:
       
        try:
            name, rest = email.split('@')
            mail, domain = rest.split('.')
        except ValueError:
            return False 
      
        return (self.__validate_name(name) and
                self.__validate_mail(mail) and
                self.__validate_domain(domain))


# Test Code
mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)

print(email_validator.validate("pe77er@gmail.com"))       # Output: True
print(email_validator.validate("georgios@gmail.net"))     # Output: False
print(email_validator.validate("stamatito@abv.net"))      # Output: False
print(email_validator.validate("abv@softuni.bg"))         # Output: False


