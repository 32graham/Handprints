DROP TRIGGER IF EXISTS tickets_tickettierchange_trigger;

CREATE FUNCTION insert_tier_change()
RETURNS trigger AS '
BEGIN
    INSERT INTO tickets_tickettierchange
    (
        ticket_id,
        date_time,
        new_tier_id,
        old_tier_id,
        user_id
    )
    VALUES
    (
        new.id,
        datetime('now'),
        new.tier_id,
        old.tier_id,
        new.user_changed_id
    );
    RETURN NEW;
END' LANGUAGE 'plpgsql'

CREATE TRIGGER tickets_tickettierchange_trigger AFTER UPDATE OF tier_id
ON tickets_ticket
WHEN new.tier_id <> old.tier_id
EXECUTE PROCEDURE insert_tier_change()
