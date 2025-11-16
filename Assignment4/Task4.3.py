def format_name(full_name):
    """Format a full name as 'Last, First'."""
    parts = full_name.strip().split()
    if len(parts) >= 2:
        first = parts[0]
        last = parts[-1]
        return f"{last}, {first}"
    else:
        return full_name  # return as-is if only one name is given
