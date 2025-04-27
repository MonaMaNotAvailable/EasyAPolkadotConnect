from sqlalchemy.orm import Session
from app import models

def create_time_slot(db: Session, slot_data: models.TimeSlotCreate):
    db_slot = models.TimeSlot(**slot_data.dict())
    db.add(db_slot)
    db.commit()
    db.refresh(db_slot)
    return db_slot

def place_bet(db: Session, time_slot_id: int, bet_data):
    db_bet = models.Bet(time_slot_id=time_slot_id, **bet_data.dict())
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet

def close_time_slot(db: Session, time_slot_id: int):
    bets = db.query(models.Bet).filter(models.Bet.time_slot_id == time_slot_id).all()
    if not bets:
        return "No bets placed."

    # Pick the highest bidder (first come, first serve in case of a tie)
    winner = max(bets, key=lambda x: x.amount)

    # Refund the losers
    refund_losers(db, bets, winner)

    # Allocate funds based on distribution rule
    slot = db.query(models.TimeSlot).filter(models.TimeSlot.id == time_slot_id).first()
    if slot.distribution_rule == "return_to_winner":
        send_funds_to_winner(winner)
    elif slot.distribution_rule == "use_for_coffee":
        send_funds_to_coffee_shop()

    slot.is_open = False
    db.commit()
    return {"winner": winner.bidder_wallet}

# --------------------
# Helper functions
# --------------------

def refund_losers(db: Session, bets, winner):
    for bet in bets:
        if bet.id != winner.id:
            # TODO: implement actual refund on-chain
            pass  # placeholder

def send_funds_to_winner(winner):
    # TODO: implement sending the pooled fund to winner
    pass  # placeholder

def send_funds_to_coffee_shop():
    # TODO: implement payment to coffee shop
    pass  # placeholder
