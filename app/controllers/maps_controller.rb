class MapsController < ApplicationController
  def index
    @addresses = Map.fetch_addresses
  end
end
