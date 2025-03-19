useEffect(() => {
    fetch('/api')
      .then((response) => response.json())
      .then((data) => console.log(data))
      .catch((error) => console.error('Erreur:', error));
  }, []);
  