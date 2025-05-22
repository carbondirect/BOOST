;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "BOOST_standard"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "a4paper" "margin=1in") ("hyperref" "") ("graphicx" "") ("enumitem" "") ("titlesec" "") ("fancyhdr" "") ("datetime" "")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "geometry"
    "hyperref"
    "graphicx"
    "enumitem"
    "titlesec"
    "fancyhdr"
    "datetime")
   (LaTeX-add-labels
    "sec:schema"))
 :latex)

