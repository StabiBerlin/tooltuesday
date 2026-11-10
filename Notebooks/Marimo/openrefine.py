import marimo

__generated_with = "0.25.1"
app = marimo.App(
    width="medium",
    layout_file="layouts/openrefine.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Stabi Tool Tuesday
    10.11.2026
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Datenstrukturierung mit OpenRefine
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Tool Tuesday
    Ein Raum, um DH-Methoden und tools zu lernen... auszuprobieren... zu experimentieren...
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ...manchmal auch zu scheitern?
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## NO CODE
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    weitgehend jedenfalls
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### Folien und weitere Materialien
    finden sich hier: https://github.com/stabiberlin/tooltuesday

    Die heutigen Folien: https://stabiberlin.github.io/tooltuesday/openrefine.html
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Überblick über die Reihe


    - Datenquellen und Schnittstellen
    - **Datenstrukturierung mit OpenRefine**
    - Automatische Texterkennung (OCR/HTR)
    - Topic Modeling
    - Netzwerkvisualierung (Gephi)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    Orientiert an einer (prototypischen) DH-'pipeline'

    Forschungsidee/Forschungsfrage

    ↪ Daten suchen (und finden); Daten generieren

    ↪ **Daten aufbereiten**

    ↪ Daten auswerten, transformieren

    ↪ Ergebnisse (und neue Daten) publizieren/visualisieren
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## OpenRefine

    - Bereinigung und Umwandlung von **strukturierten** Daten
    - Daten anreichern
    - Unstrukturierten Text (re)strukturieren

    ---

    https://openrefine.org/

    Installation: https://openrefine.org/docs/manual/installing
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Einstieg, Datenbereinigung
    """)
    return


@app.cell
def _(mo):
    mo.image(src="public/names.png", height=500)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Einstieg, Datenbereinigung

    - Import
    - Filter
    - Facetten
    - Sortieren
    - Daten korrigieren
    - Datentypen anpassen
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    #### Einstieg, Datenbereinigung: Daten clustern"""),
            mo.image(src="public/cluster.png", height=500),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Einstieg, Datenbereinigung

    - Export
    - Speichern
    - Import
    - Undo/Redo
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Arbeiten mit strukturierten Daten
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Schnittstellenabfrage

    Beispiel: [Nachlass Werner Heisenberg](https://kalliope-verbund.info/ead?ead.id=DE-611-BF-73161) im Kalliope-Verbundkatalog

    ```
     https://kalliope-verbund.info/sru?version=1.2&operation=searchRetrieve&query=ead.archdesc.id=%22DE-611-BF-73161%22%20AND%20ead.unitdate_start%3E=1945%20AND%20ead.unitdate_end%3C=1945&recordSchema=dc
    ```

    [Abfrage 1945](https://kalliope-verbund.info/sru?version=1.2&operation=searchRetrieve&query=ead.archdesc.id=%22DE-611-BF-73161%22%20AND%20ead.unitdate_start%3E=1945%20AND%20ead.unitdate_end%3C=1945&recordSchema=dc)

    [Schnittstellenbeschreibung](https://lab.sbb.berlin/kpe/)
    """)
    return


@app.cell
def _(mo):
    _text = mo.md(r"""
    #### Schnittstellenabfrage
    - Record vs. Row
    - Filtern
    - Join/Split
    """)

    mo.hstack([_text, mo.image(src="public/letters.png", height=500)])
    return


@app.cell
def _(mo):
    mo.vstack([mo.md(r"""
    #### Weitere Schnittstellenabfrage


    ```
     https://kalliope-verbund.info/sru?version=1.2&operation=searchRetrieve&query=ead.id=DE-611-HS-3648708&recordSchema=mods

    ```

    [Abfrage Einzelbrief](https://kalliope-verbund.info/sru?version=1.2&operation=searchRetrieve&query=ead.archdesc.id=%22DE-611-BF-3872%22&recordSchema=dc&maximumRecords=17&startRecord=616)

    #### Parsen
    """),
    mo.image(src="public/parseXml.png", height=450)])
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    #### Textmanipulationen

    [Brief von Magnus Hirschfeld an Gerhart Hauptmann](https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=PPN771823622&PHYSID=PHYS_0001&DMDID=)"""),
            mo.image(src="public/wlsr.png", height=450),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Textmanipulationen

    - split
    - replace
    - Reguläre Ausdrücke ([regex101](https://regex101.com), [regexlearn](https://regexlearn.com/))
    """)
    return


@app.cell
def _(mo):
    mo.vstack([mo.md(r"""
    #### Unstrukturierten Text (re)strukturieren
    """), mo.image(src="public/split.png", height=500)])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Reconciliation

    Abgleich von Daten mit externen Datenbeständen (Normdaten, Wikidata, ...)

    [Reconciliation Services](https://reconciliation-api.github.io/testbench/#/)
    """)
    return


@app.cell
def _(mo):
    mo.image(src="public/reconcile.png", height=500)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Teaser
    #### KI & OpenRefine
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### KI & OpenRefine

    Extension: https://github.com/sunilnatraj/llm-extension

    https://openrefine.org/docs/manual/installing#installing-extensions

    Voraussetzung: API-Key eines KI-Providers
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    #### KI & OpenRefine"""),
            mo.image(src="public/ai.png", height=450),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Projekt (siehe [hier](https://github.com/StabiBerlin/tooltuesday/blob/main/CroniclingAmericaSuffrage.openrefine.tar.gz))
    Volltexte aus [Chronicling America](https://www.loc.gov/collections/chronicling-america/?q=suffrage), Stichwort "Suffrage"

    #### Prompt
    ```
    You are an expert in historical newspapers and historical womens' rights movements.

    You will read the OCRed page of a historical newspaper, dating from 1870 to 1910.
    In some sections "suffrage" should be mentioned.

    There will be OCR errors in the text - try to ignore them as best as possible.

    Please summarize the relevant sections. Do not return the text of the relevant section.
    ```
    """)
    return


@app.cell
def _(mo):
    mo.vstack(
        [
            mo.md(r"""
    #### KI & OpenRefine: Ergebnis"""),
            mo.image(src="public/summary.png", height=450),
        ]
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Weitere Informationen

    [OpenRefine-Dokumentation](https://openrefine.org/docs)

    [OpenRefine-Forum](https://forum.openrefine.org/)

    [LibraryCarpentry-Lesson](https://librarycarpentry.github.io/lc-open-refine/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Danke für die Aufmerksamkeit
    01.12.2026 Automatische Texterkennung (OCR/HTR)
    """)
    return


if __name__ == "__main__":
    app.run()
