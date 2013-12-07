CREATE OR REPLACE FUNCTION insert_tier_change()
RETURNS trigger AS '
BEGIN
    INSERT INTO tickets_tickettierchange
    (
        ticket_id,
        date_time,
        new_tier_id,
        old_tier_id,
        profile_id
    )
    VALUES
    (
        new.id,
        NOW(),
        new.tier_id,
        old.tier_id,
        new.profile_changed_id
    );
    RETURN NEW;
END' LANGUAGE 'plpgsql';

CREATE TRIGGER tickets_tickettierchange_trigger AFTER UPDATE OF tier_id
ON tickets_ticket
FOR EACH ROW
WHEN (NEW.tier_id <> OLD.tier_id)
EXECUTE PROCEDURE insert_tier_change();

CREATE OR REPLACE FUNCTION insert_status_change()
RETURNS trigger AS '
BEGIN
    INSERT INTO tickets_ticketstatuschange
    (
        ticket_id,
        date_time,
        new_status_id,
        old_status_id,
        profile_id
    )
    VALUES
    (
        new.id,
        NOW(),
        new.status_id,
        old.status_id,
        new.profile_changed_id
    );
    RETURN NEW;
END' LANGUAGE 'plpgsql';

CREATE TRIGGER tickets_ticketstatuschange_trigger AFTER UPDATE OF status_id
ON tickets_ticket
FOR EACH ROW
WHEN (NEW.status_id <> OLD.status_id)
EXECUTE PROCEDURE insert_status_change();
