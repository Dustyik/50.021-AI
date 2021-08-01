(define (problem LogisticProblem)
    (:domain logistic-domain)
    (:objects p1 p2 Changi Tampinese Bedok ninjaVan)
    (:init 
        (package p1) (package p2)
        (location Bedok) (location Tampinese) (location Changi)
        (truck ninjaVan) 
        (at-location p1 Bedok) (at-location p2 Changi) 
        (at-location ninjaVan Tampinese) 
    )
    (:goal (and (at-location p1 Changi) (at-location p2 Bedok) 
            (not (carry p1 ninjaVan)) (not (carry p2 ninjaVan))
            )
    )
)
