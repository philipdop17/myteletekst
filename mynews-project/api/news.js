export default async function handler(req, res) {
  const category = req.query.category || 'general';
  const apiKey = '08f6e8882a204261af7ef19be1f68aaa'; // or use env variable later
  const url = `https://newsapi.org/v2/top-headlines?country=us&category=${category}&apiKey=${apiKey}`;

  try {
    const response = await fetch(url);
    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch news' });
  }
}