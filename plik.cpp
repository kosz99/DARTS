#include <fstream>
class Document
{
public:
  Data d;
  std::string t;
  
//  Konstruktor
  Document(std::string title, Data data)
  {
      d = data;
      t = title;
  }
    
  void save(std::string_view fileName)
  {
    std::ofstream out(fileName);
    out << title();
    out << "\n";
    out << data(); // typ Data poprawnie zachowa swoje dane w tej operacji
    out << "\n.\n";
    
    out.close()
  }
//title setter
  void set_title(std:string title)
  {
      t = title;
  }
//data setter
  void set_data(Data data)
  {
      d = data;
  }
    
  std::string title() const;
  Data data() const; // typ Data nieistotny dla reszty problemu
  void combine(const Data& other)
  {
    // szczegóły implementacji nie mają znaczenia
  }
};

std::string Document::title() const
{
    return t;
}

Data Document::data() const
{
    return d;
}
