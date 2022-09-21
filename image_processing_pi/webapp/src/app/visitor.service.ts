import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class VisitorService {

  constructor(private _http: HttpClient) { }

  serverUrl = 'http://127.0.0.1:5000';

  saveDataset() {
    console.log('visitor service save dataset is called');
    return this._http.get('http://127.0.0.1:5000/save_dataset');
  }

  getInfo() {
    return this._http.get(this.serverUrl + '/save_dataset');
  }

  saveInfo(data){
    return this._http.post(this.serverUrl + '/save_dataset', data);
  }
}
