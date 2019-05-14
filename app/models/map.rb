class Map 
  def self.fetch_addresses
    `python lib/assets/get_addresses.py`
  end
end
