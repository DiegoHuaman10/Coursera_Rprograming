
# Create a special "array" object that caches its inverse.
makeCacheMatrix <- function(m = matrix()) {
  matriz <- m
  cache <- NULL
  set <- function(mat) {
    matriz <<- mat
    cache <<- NULL
  }
  
  # Función para obtener la matriz Function for get matrix
  get <- function() matriz
  
  # Función para calcular la inversa de la matriz
  cacheSolve <- function() {
    if (!is.null(cache)) {
      message("Recuperando inversa desde la caché")
      return(cache)
    }
    # Calcular la inversa
    inversa <- solve(matriz)
    cache <<- inversa
    inversa
  }
  
  # Devolver las funciones como una lista
  list(set = set, get = get, cacheSolve = cacheSolve)
}



