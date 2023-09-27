def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    verify_entries = 0
    for entries, exits in permanence_period:
        if type(entries) != int or type(exits) != int:
            return None
        if entries <= target_time <= exits:
            verify_entries += 1
    return verify_entries
