#!/usr/bin/env python
# --!-- coding: utf8 --!--

from manuskript.exporter.basic import basicExporter, basicFormat

class HTMLFormat(basicFormat):
    name = "HTML"
    description = "A little known format modestly used. You know, web sites for example."
    implemented = False
    requires = {
        "Settings": True,
        "PreviewBefore": True,
        "PreviewAfter": True,
    }


class pandocExporter(basicExporter):

    name = "Pandoc"
    description = """<p>A universal document convertor. Can be used to convert markdown to a wide range of other
    formats.</p>
    <p>Website: <a href="http://www.pandoc.org">http://pandoc.org/</a></p>
    """
    exportTo = [
        HTMLFormat,
        basicFormat("ePub", "Books that don't kill trees."),
        basicFormat("OpenDocument", ""),
        basicFormat("PDF", "Needs latex to be installed."),
        basicFormat("DocX", "Microsoft Office (.docx) document."),
    ]
    cmd = "pandoc"

    @classmethod
    def version(cls):
        if cls.isValid():
            r = cls.run(["-v"])
            return r.split("\n")[0]
        else:
            return ""



