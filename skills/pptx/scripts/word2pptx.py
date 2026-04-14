"""Word to PPTX converter.
Usage: python word2pptx.py <input.docx> <output.pptx>
"""
import sys
import os
from docx import Document
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RgbColor
from pptx.enum.text import PP_ALIGN

def docx_to_pptx(docx_path, pptx_path):
    """Convert a Word document to PowerPoint."""
    doc = Document(docx_path)
    prs = Presentation()
    
    # Get document title from first paragraph
    title = "Presentation"
    slides_data = []
    current_title = None
    current_bullets = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
            
        style_name = para.style.name if para.style else ""
        
        if "Heading" in style_name or style_name.startswith("Title"):
            if current_title and current_bullets:
                slides_data.append({
                    "title": current_title,
                    "bullets": current_bullets[:]
                })
            current_bullets = []
            current_title = text
            if not title or style_name.startswith("Title"):
                title = text
        else:
            if current_title is None:
                current_title = title
            current_bullets.append(text)
    
    if current_title and current_bullets:
        slides_data.append({"title": current_title, "bullets": current_bullets})
    
    if not slides_data:
        slides_data = [{"title": title, "bullets": [p.text.strip() for p in doc.paragraphs[:10] if p.text.strip()]]}]
    
    # Title slide
    ts = prs.slides.add_slide(prs.slide_layouts[6])
    tb = ts.shapes.add_textbox(Inches(1), Inches(2.5), Inches(8), Inches(1.5))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    
    # Content slides
    for sd in slides_data:
        s = prs.slides.add_slide(prs.slide_layouts[6])
        
        tb = s.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(1))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        p.text = sd["title"]
        p.font.size = Pt(28)
        p.font.bold = True
        
        bb = s.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5))
        tf = bb.text_frame
        tf.word_wrap = True
        
        for i, b in enumerate(sd["bullets"][:8]):
            bp = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            bp.text = "- " + b
            bp.font.size = Pt(17)
            bp.space_after = Pt(8)
    
    prs.save(pptx_path)
    return len(slides_data) + 1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python word2pptx.py input.docx output.pptx")
        sys.exit(1)
    
    n = docx_to_pptx(sys.argv[1], sys.argv[2])
    print(f"Created {n} slides -> {sys.argv[2]}")
