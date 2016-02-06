(defn hyfact [n]
  "Lisp in Python!"
  (defn fact-impl [n acc]
    (if (<= n 1)
        acc
      (fact-impl (- n 1) (* acc n))))
  (fact-impl n 1))
