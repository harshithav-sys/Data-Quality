from check.sugar_check import python_check_sugar, perl_check_sugar
from check.name_check import python_check_name, perl_check_name
from check.salt_check import python_check_salt, perl_check_salt


def validate_product(product):
    results = {}

    results["sugar"] = compare(
        perl_check_sugar(product["sugar"]),
        python_check_sugar(product["sugar"])
    )

    results["name"] = compare(
        perl_check_name(product["name"]),
        python_check_name(product["name"])
    )

    results["salt"] = compare(
        perl_check_salt(product["salt"]),
        python_check_salt(product["salt"])
    )

    return results


def compare(perl_result, python_result):
    return {
        "perl": perl_result,
        "python": python_result,
        "status": "PASS" if perl_result == python_result else "FAIL"
    }