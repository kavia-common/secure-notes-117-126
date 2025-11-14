from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas, models, auth

router = APIRouter()

# PUBLIC_INTERFACE
@router.get("/", response_model=schemas.NotesList, summary="List notes", description="Get all notes belonging to the logged-in user")
def list_notes(current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(auth.get_db)):
    notes = db.query(models.Note).filter(models.Note.owner_id == current_user.id).all()
    return schemas.NotesList(notes=notes)

# PUBLIC_INTERFACE
@router.post("/", response_model=schemas.NoteOut, summary="Create note", description="Create a note for the logged-in user")
def create_note(note: schemas.NoteCreate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(auth.get_db)):
    db_note = models.Note(content=note.content, owner_id=current_user.id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# PUBLIC_INTERFACE
@router.put("/{note_id}", response_model=schemas.NoteOut, summary="Update note", description="Update a specific note of the logged-in user")
def update_note(note_id: int, update: schemas.NoteUpdate, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(auth.get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")
    db_note.content = update.content
    db.commit()
    db.refresh(db_note)
    return db_note

# PUBLIC_INTERFACE
@router.delete("/{note_id}", status_code=204, summary="Delete note", description="Delete a specific note of the logged-in user")
def delete_note(note_id: int, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(auth.get_db)):
    db_note = db.query(models.Note).filter(models.Note.id == note_id, models.Note.owner_id == current_user.id).first()
    if not db_note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found.")
    db.delete(db_note)
    db.commit()
    return
