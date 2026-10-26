import marimo

__generated_with = "0.25.2"
app = marimo.App(
    width="medium",
    layout_file="layouts/datenquellen.slides.json",
    css_file="custom.css",
)


@app.cell
def _():
    import marimo as mo

    LIVE = True  # set to True while developing, False before exporting
    return LIVE, mo


@app.cell
def _(mo):
    mo.md("""
    # Stabi Tool Tuesday
    27.10.2026
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ## Datenquellen
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

    Die heutigen Folien: https://stabiberlin.github.io/tooltuesday/slides/datenquellen.html
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Intro
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Über mich
    - Literaturwissenschaftler (analog ausgebildet)
    - [Stabi Lab](lab.sbb.berlin)
    - kein Programmierer ... aber interessiert an digitalen Methoden



    roman.kuhn@sbb.spk-berlin.de
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Überblick über die Reihe


    - **Datenquellen und Schnittstellen**
    - Datenstrukturierung mit OpenRefine
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

    ↪ Daten aufbereiten

    ↪ Daten auswerten, transformieren

    ↪ Ergebnisse (und neue Daten) publizieren/visualisieren
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Datenquellen

    Woher bekommen wir unsere Daten???
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Repositorien und Datensets
    Repositorien und Datensets
    https://www.deutschestextarchiv.de/

    https://dracor.org/

    https://textgridrep.org/

    ↪ z.B. https://textgridrep.org/project/TGPR-99d098e9-b60f-98fd-cda3-6448e07e619d

    https://www.eighteenthcenturypoetry.org/

    ↪ https://github.com/alhuber1502/ECPA

    https://lab.sbb.berlin/datenset-transkriptionen-julie-elias/
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Suchmaschinen


    https://explore.openaire.eu/

    https://registry.text-plus.org/

    https://www.base-search.net/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Schnittstellen (APIs)
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    Eine API ist eine Schnittstelle, über die Programme und Menschen per URL **strukturierte** Daten bei einem Server abfragen.


    #### Worauf man bei APIs achten sollte

    | | |
    |---|---|
    | 🔑 **Schlüssel** | Manche APIs brauchen einen Key (Registrierung), andere nicht. Den Schlüssel nicht öffentlich teilen! |
    | ⏱ **Limits** | Anfragen pro Minute oder Tag können begrenzt sein. Höflich bleiben, Pausen einbauen, große Mengen als Download holen, wenn es das gibt. |
    | 🆔 **Identifier** | Der Schlüssel zu den Daten. *Welche* ID ein Dienst erwartet ist von Institution zu Institution unterschiedlich ('ARK', 'PPN', etc. pp.) |
    | 🔗 **Mehrere APIs** | Ein Dienst liefert selten alles. Katalog-API → Identifier → Bild-API. |
    | 📄 **Seiten** | Ergebnisse kommen evtl. portionsweise (z. B. 10 pro Anfrage). „Alles" heißt: weiterblättern, über Parameter wie `start` oder ein `resumptionToken`. |
    """)
    return


@app.cell(hide_code=True)
def _(mo):

    mo.vstack(
        [
            mo.md(r"""
    #### Aufgabe"""),

    mo.hstack(
        [
            mo.md("""Ziel ist es, alle Ausgaben der Zeitschrift "Nouveau Mercure Galant" aus Gallica herunterzuladen"""),
            mo.image(src="public/mercure.jpg", width=500),
        ],
        justify="start",
        gap=2,
        align="center",
    )]
    )
    return


@app.cell
def _(LIVE, mo):
    if LIVE:
        _out = mo.Html(
        """
        <iframe src="https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&query=%28dc.title%20all%20%22Nouveau%20Mercure%20galant%22%29&keywords=Nouveau%20Mercure%20galant&suggest=3"
                style="width: 100%; height: 70vh; border: 0;"
                loading="lazy"></iframe>
        """
    )
    else:

        _img = mo.image(src="public/gallica.jpg", width=1200)
        _out = mo.Html(f"""
          <a href="https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&query=%28dc.title%20all%20%22Nouveau%20Mercure%20galant%22%29&keywords=Nouveau%20Mercure%20galant&suggest=3" target="_blank" rel="noopener">
            {_img.text}
          </a>

        """)

    _out

    return


@app.cell
def _(mo):
    _img = mo.image(src="public/gallica_api.png", width=1200)

    mo.Html(f"""
      <a href="https://api.bnf.fr/fr/api-document-de-gallica" target="_blank" rel="noopener">
        {_img.text}
      </a>

    """)
    return


@app.cell
def _(mo):
    mo.md("""
    https://gallica.bnf.fr/services/Issues?ark=cb40216990r

    ```xml
    <issues compile_time="0:00:00.019" listType="years" parentArk="cb40216990r/date" totalIssues="28">
      <year>1714</year>
      <year>1715</year>
      <year>1716</year>
    </issues>
    ```
    https://gallica.bnf.fr/services/Issues?ark=cb40216990r&date=1714

    ```xml
    <issues compile_time="0:00:01.380" date="1714" listType="issue" parentArk="cb40216990r/date" data-google-analytics-opt-out="\">
    <issue ark="bpt6k63194664" dayOfYear="1"> 1714</issue>
    <issue ark="bpt6k63197487" dayOfYear="1"> 1714</issue>
    <issue ark="bpt6k6338506f" dayOfYear="121">01 mai 1714</issue>
    <issue ark="bpt6k6328421h" dayOfYear="182">01 juillet 1714</issue>
    <issue ark="bpt6k6338504m" dayOfYear="244">01 septembre 1714</issue>
    <issue ark="bpt6k6348102p" dayOfYear="305">01 novembre 1714</issue>
    <issue ark="bpt6k6338236j" dayOfYear="335">01 décembre 1714</issue>
    </issues>
    ```
    """)
    return


@app.cell
def _(mo):
    _img = mo.image(src="public/gallica_text.jpg", width=1200)

    mo.vstack([mo.md("""
    https://gallica.bnf.fr/ark:/12148/bpt6k63194664.texteBrut
    """),
              mo.Html(f"""
      <a href="https://gallica.bnf.fr/ark:/12148/bpt6k63194664.texteBrut" target="_blank" rel="noopener">
        {_img.text}
      </a>

    """)])
    return


@app.cell
def _(mo):
    mo.md("""
    #### LLM der Wahl
    ```
    Du hilfst mir, die API von Gallica (BnF) ohne Programmierung zu nutzen.

    Aufgabe: Ich möchte alle **Volltexte** Ausgaben der Zeitschrift "Nouveau Mercure galant"
    aus dem Jahr 1714 herunterladen. Die ARK der Zeitschrift ist cb40216990r.

    Regeln:
    - Verwende AUSSCHLIESSLICH die Dokumentation unten. Erfinde keine
      Endpunkte oder Parameter.
    - Wenn die Dokumentation für die Aufgabe nicht ausreicht, sag das
      ausdrücklich, statt zu raten.
    - Gib mir eine fertige URL, die ich im Browser öffnen kann.
    - Erkläre danach jeden Teil der URL in einer Zeile (Basis, Endpunkt,
      Parameter).
    - Nenne am Ende, was du dir nicht sicher bist.

    Dokumentation:
    https://api.bnf.fr/fr/api-document-de-gallica
    ```
    """)
    return


@app.cell
def _(mo):
    mo.vstack([
    mo.hstack(
        [
            mo.image(src="public/claude_gall1.jpg", width=800),
            mo.image(src="public/claude_gall2.jpg", width=800),
        ],
        justify="start",
        gap=2,
        align="center",
    ),
    mo.md("Claude Sonnet 5.5, thinking=Mittel")])
    return


@app.cell
def _(mo):
    _img = mo.image(src="public/dpla.png", width=1200)

    mo.hstack([
    mo.Html(f"""
      <a href="https://dp.la/search?q=Suffrage&type=%22physical+object%22&page=1&after=1880&before=1920" target="_blank" rel="noopener">
        {_img.text}
      </a>

    """), mo.image(src="public\dpla-api.jpg")])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Verbreitete Standards in Bibliotheken
    - IIIF - Bilder
    - OAI-PMH - Metadaten (Austausch)
    - SRU - Metadaten (Suche)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Schnittstellen der Staatsbibliothek

    Für bibliographische Daten aus dem Stabikat: https://lab.sbb.berlin/bibliographische-daten-aus-dem-stabikat/ (SRU)

    Für Daten aus den Digitalisierten Sammlungen https://lab.sbb.berlin/dc/ (OAI & IIIF)

    Notebooks mit detaillierten Beschreibungen: https://lab.sbb.berlin/oai-schnittstellen-mit-python/
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### IIIF: Bilder als API

    **International Image Interoperability Framework**

    - Ein Bild ist über eine **URL** abrufbar, und diese beschreibt, *wie* es geliefert wird
    - Ausschnitt, Größe, Drehung und Format steuern wir selbst, ohne das Original herunterzuladen



    | API | Frage |
    |---|---|
    | **[Image API](https://iiif.io/api/image/3.0/)** | Wie bekomme ich *dieses Bild* in *dieser Form*? |
    | **[Presentation API](https://iiif.io/api/presentation/3.0/)** | Was gehört zusammen, und in welcher Reihenfolge? |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Die Image API

    ```

    https://iiif.wellcomecollection.org/image/V0023904/100,100,250,250/800,/180/default.jpg
    -----------Basis ------------------------/ Bild --/----Region-----/Größe/Rot/Qual.Format

    ```

    `{Basis}/{Identifier}/{Region}/{Größe}/{Drehung}/{Qualität}.{Format}`


    Wichtig: Die URL liefert nur *ein Bild*. Zu welchem Werk dieses Bild evtl. gehört, was davor und danach kommt, steht dort nicht.
    """)
    return


@app.cell
def _(mo):
    rotation = mo.ui.slider(start=0, stop=360, label="Rotation", value=0, full_width=True)
    x_slider = mo.ui.range_slider(start=0, stop=3250, step=2, value=[0, 3250], full_width=True)
    y_slider = mo.ui.range_slider(start=0, stop=2191, step=2, value=[0, 2191], full_width=True)
    size =  mo.ui.dropdown(
                        {"Breite 800": "800,", "Breite 200": "200,", "Höhe 400": ",400",
                         "25 %": "pct:25", "verzerrt 400×400": "400,400",
                         "einpassen !400,400": "!400,400", "Original": "max"},
                        value="Breite 800", label="Größe")
    return rotation, size, x_slider, y_slider


@app.cell
def _(LIVE, mo, rotation, size, x_slider, y_slider):
    if LIVE:


        region = f"{x_slider.value[0]},{y_slider.value[0]},{x_slider.value[1] - x_slider.value[0]},{y_slider.value[1] - y_slider.value[0]}"
        print(region)
        _out = mo.vstack(
            [rotation, 
             size,
             x_slider,
             y_slider,
             mo.md(f"URL: https://iiif.wellcomecollection.org/image/V0023904/{region}/{size.value}/{rotation.value}/default.jpg"),
             mo.Html(f"""
        <iframe src="https://iiif.wellcomecollection.org/image/V0023904/{region}/{size.value}/{rotation.value}/default.jpg"
                style="width: 100%; height: 70vh; border: 0;"
                loading="lazy"></iframe>
        """
    )])

    else:

        _img = mo.image(src="public/gallica.jpg", width=1200)
        _out = mo.Html(f"""
          <a href="https://gallica.bnf.fr/services/engine/search/sru?operation=searchRetrieve&version=1.2&query=%28dc.title%20all%20%22Nouveau%20Mercure%20galant%22%29&keywords=Nouveau%20Mercure%20galant&suggest=3" target="_blank" rel="noopener">
            {_img.text}
          </a>

        """)
    #rotation
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Manifeste: Was gehört zusammen?

    Ein **Manifest** ist eine JSON-Datei, die ein digitalisiertes Objekt beschreibt:

    - **Titel, Lizenz, Metadaten**
    - **Canvases:** eine „Leinwand" pro Seite, mit Breite und Höhe
    - **Verweis auf den Bilddienst** jeder Seite
    - Möglicherweise weitere Daten: **Volltext** o.ä.

    Viewer wie Mirador oder der Universal Viewer lesen das Manifest und holen sich die Bilder über die Image API.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.vstack(
        [mo.md(r"""
    Katalogeintrag: https://wellcomecollection.org/works/qr4m23px

    IIIF-Manifest: https://iiif.wellcomecollection.org/presentation/v2/b33278787
    """),
    mo.hstack([mo.vstack([mo.md("Öffnen im [Handschriftenportal](https://handschriftenportal.de/workspace)"), mo.image(src="public/hsp.jpg", width=700)]),
               mo.image(src="public/iiif.jpg", width=700)
              ])
        ])
    return


@app.cell
def _(mo):
    mo.md("""
    #### Metadaten aus den Digitalisierten Sammlungen der Stabi über OAI

    https://oai.sbb.berlin/?verb=Identify

    https://oai.sbb.berlin/?verb=ListSets

    https://oai.sbb.berlin/?verb=ListIdentifiers&metadataPrefix=oai_dc&set=adelbert.von.chamisso


    ```
    {base}?verb={Aktion}&metadataPrefix{Metadatenschema}&set{Setname}
    ```

    Verfügbare Aktionen: Identify | ListRecords  | ListSets | ListMetadataFormats | ListIdentifiers
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    #### Metadaten aus dem K10Plus-Verbundkatalog über SRU
    https://sru.k10plus.de/opac-de-627?recordSchema=dc&operation=searchRetrieve&version=1.1&maximumRecords=100&query=pica.per=Voltaire

    Beispiel: Abfrage und Auswertung von Provenienzmerkmalen [![Open with marimo](https://marimo.io/shield.svg)](https://marimo.app/?src=https://github.com/StabiBerlin/Provenienz_SRU/blob/main/sru_provenienz_embed.py&mode=run&show-code=false)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Weitere Schnittstellen

    https://pro.europeana.eu/discover-the-data/apis

    https://pro.dp.la/developers/api-codex

    https://pro.deutsche-digitale-bibliothek.de/daten-nutzen/schnittstellen

    [Smithsonian](https://edan.si.edu/openaccess/apidocs/)

    [archive.org](https://archive.org/developers/index-apis.html)

    etc. pp.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Danke für die Aufmerksamkeit
    10.11.2026 Datenstrukturierung mit [OpenRefine](https://openrefine.org/)

    (Software gerne vorab downloaden & installieren)
    """)
    return


if __name__ == "__main__":
    app.run()
