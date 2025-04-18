
def get_hr_score(barrel_rate, exit_velocity, xSLG, sweet_spot, rpi,
                 hr9, hard_hit_pct, fatigue,
                 park_factor, wind_boost, temp_boost):
    # Calculate Batter Power Score (50%)
    bps = (barrel_rate * 1.5 + exit_velocity * 0.5 + xSLG * 100 + sweet_spot * 0.5 + rpi * 100) / 5
    
    # Calculate Pitcher Vulnerability Score (30%)
    pvs = (hr9 * 30 + hard_hit_pct * 0.5 + fatigue * 5) / 3
    
    # Contextual Adjustments (20%)
    context = park_factor + wind_boost * 0.5 + temp_boost * 0.5
    
    # Weighted score
    total = (bps * 0.5 + pvs * 0.3 + context * 0.2)
    sleeper = (rpi > 0.7 and barrel_rate > 12 and total < 85)
    return min(round(total, 1), 100), sleeper
