(define (problem LogisticProblem)
(:domain LogisticDomain>)
    (:init 
        (PACKAGE p1)
        (LOCATION Changi) (LOCATION Tampinese) (LOCATION bedok)
        (TRUCK ninjaVan) 
        (package-at-location p1 Bedok) 
        (truck-at-location ninjaVan Bedok) 
    )
    (:goal (
        and (package-at-location (p1, Changi)) 
    )
)
