from core.security_utils import validate_origin

if __name__ == "__main__":
    if validate_origin("alpha_package_metadata.json"):
        print("VALID: Project integrity confirmed.")
    else:
        print("WARNING: Unauthorized project modification detected.")