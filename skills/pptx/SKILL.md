# PPTX Skill

## Description
Create professional PowerPoint (.pptx) presentations from text content, Word documents, or outlines.

## When to Use
- User wants to create or edit .pptx files
- User wants to convert Word/docx to PowerPoint
- User needs presentation slides generated

## Prerequisites
```bash
pip install python-pptx python-docx
```

## Workflow

### From Word Document to PPTX
1. Read the Word document using python-docx
2. Extract headings, paragraphs, lists, tables
3. Create slides with python-pptx:
   - Each H1/H2 becomes a new slide title
   - Paragraphs become bullet points
   - Tables become slide tables
   - Images are embedded
4. Apply consistent theme/styling
5. Save as .pptx

### From Outline/Markdown to PPTX
1. Parse markdown structure (# ## ### for hierarchy)
2. Create title slide from first heading
3. Each subsequent ## creates new section slide
4. Bullet points from - * list items under each heading
5. Add visual elements (shapes, colors)

## Code Template

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RgbColor
from pptx.enum.text import PP_ALIGN

def create_presentation(title, slides_data, output_path):
    """Create a PPTX from structured data.
    
    Args:
        title: Presentation title string
        slides_data: List of dicts with keys:
            - 'title': slide title
            - 'bullets': list of bullet point strings
            - 'notes': optional speaker notes
        output_path: Output .pptx file path
    """
    prs = Presentation()
    
    # Title slide
    title_slide = prs.slides.add_slide(prs.slide_layouts[6])
    txBox = title_slide.shapes.add_textbox(Inches(1), Inches(2), Inches(8), Inches(2))
    tf = txBox.text_frame
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(40)
    p.font.bold = True
    p.alignment = PP_ALIGN.CENTER
    
    # Content slides
    for slide_info in slides_data:
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        
        # Slide title
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.3), Inches(9), Inches(1))
        tf = title_box.text_frame
        p = tf.paragraphs[0]
        p.text = slide_info['title']
        p.font.size = Pt(28)
        p.font.bold = True
        
        # Bullet points
        body_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5))
        tf = body_box.text_frame
        tf.word_wrap = True
        
        for i, bullet in enumerate(slide_info.get('bullets', [])):
            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()
            p.text = bullet
            p.font.size = Pt(18)
            p.level = 0
            p.space_after = Pt(10)
    
    prs.save(output_path)
    return output_path
```

## Style Guidelines
- Use consistent fonts (e.g., Microsoft YaHei for Chinese, Arial for English)
- Limit bullets to 6 per slide
- Font size: titles 28-36pt, body 16-20pt
- Use company/theme colors consistently
- Add page numbers in footer
