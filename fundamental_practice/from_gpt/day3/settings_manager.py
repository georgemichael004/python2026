# Task: Add, update, delete, and view settings in a dictionary.
settings = {}

def add_setting(settings, key, value):
    if key in settings:
        return "Setting already exists"
    settings[key] = value
    return "Setting added"

def update_setting(settings, key, value):
    if key not in settings:
        return "Setting not found"
    settings[key] = value
    return "Setting updated"

def delete_setting(settings, key):
    if key not in settings:
        return "Setting not found"
    del settings[key]
    return "Setting deleted"

def view_settings(settings):
    if not settings:
        return "No settings"
    output = ""
    for key, value in settings.items():
        output += f"{key}: {value}\n"
    return output.strip()

# Example usage
print(add_setting(settings, "theme", "dark"))
print(add_setting(settings, "language", "english"))
print(update_setting(settings, "theme", "light"))
print(delete_setting(settings, "language"))
print(view_settings(settings))

