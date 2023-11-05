
# Create a special "array" object that caches its inverse.
makeCacheMatrix <- function(ma = matrix()) {
  matriz <- ma
  cache <- NULL
  set <- function(matri) {
    matriz <<- matri
    cache <<- NULL
  }
  
  #Function to get the matrix
  get <- function() matriz
  
  # Function to calculate the inverse of the matrix
  cacheSolve <- function() {
    if (!is.null(cache)) {
      message("Retrieving the inverse from the cache")
      return(cache)
    }
    inversa <- solve(matriz)
    cache <<- inversa
    inversa
  }
  
  # Return the functions as a list
  list(set = set, get = get, cacheSolve = cacheSolve)
}



